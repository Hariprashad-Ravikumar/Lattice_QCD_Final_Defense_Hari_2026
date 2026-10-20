import sympy as s
from itertools import product
m,E,p,x,y,h,u,w=s.symbols('m E p x y eta v1 v3', real=True, nonzero=True)
a2,a3,a12,b1,b7,b8,b9,b10=s.symbols('a2 a3 a12 b1 b7 b8 b9 b10')
P=[E,-p,0,0];b=[0,x,y,0];v=[0,u,0,w];S=[0,0,0,1];g=[1,-1,-1,-1]
Pc,Bc,Vc,Sc=[[g[j]*q[j] for j in range(4)] for q in [P,b,v,S]]
vs=-w
F=[]
for mu in range(4):
 f=P[mu]*a2-s.I*m*m*b[mu]*a3+m*m*h*v[mu]*b1
 for n,al,be in product(range(4), repeat=3):
  ep=s.LeviCivita(mu,n,al,be)
  f+=ep*(-s.I*m*Pc[n]*Bc[al]*Sc[be]*a12+m*h*Pc[n]*Vc[al]*Sc[be]*b7-s.I*m**3*h*Bc[n]*Vc[al]*Sc[be]*b8-s.I*m**3*vs*Pc[n]*Bc[al]*h*h*Vc[be]*b10)
 F.append(s.expand(f))
ratios=[s.I*F[1]/E,-s.I*F[2]/E,s.I*F[3]/E,F[0]/E]
expected=[-s.I*p/E*a2+m*m*x/E*a3+s.I*m*m*h*u/E*b1-m*y*a12+m**3*y*h*h*w*w*b10,-m*m*y/E*a3-m*x*a12-s.I*m*h*u*b7+m**3*x*h*h*w*w*b10,s.I*m*m*h*w/E*b1-m**3*y*h*h*u*w*b10,a2-s.I*m*p/E*y*a12-s.I*m**3/E*y*h*u*b8+s.I*m**3/E*p*y*h*h*w*w*b10]
assert all(s.simplify(a-b)==0 for a,b in zip(ratios,expected))
ars=s.symbols('ar2 ar3 ar12 br1 br7 br8 br10',real=True); ais=s.symbols('ai2 ai3 ai12 bi1 bi7 bi8 bi10',real=True)
amp=[a2,a3,a12,b1,b7,b8,b10]
plus=[s.expand(2*r.subs(dict(zip(amp,[ar+s.I*ai for ar,ai in zip(ars,ais)])))) for r in ratios]
minus=[s.expand(r.subs(x,-x).subs(dict(zip(ais,[-ai for ai in ais])))) for r in plus]
even=[s.expand((a+b)/2) for a,b in zip(plus,minus)];odd=[s.expand((a-b)/2) for a,b in zip(plus,minus)]
aR2=s.re(even[3])/2; bR1=E/(2*m*m*h*w)*s.im(even[2]);aR12=-(s.re(even[0])+w/u*s.re(even[2]))/(2*m*y);bR8=-E/(2*m**3*y*h*u)*(s.im(even[3])+p*w/(E*u)*s.re(even[2])+2*m*p/E*y*aR12)
aI2=s.im(odd[3])/2;bI1=-E/(2*m*m*h*w)*s.re(odd[2]);aI12=-(s.im(odd[0])+w/u*s.im(odd[2]))/(2*m*y);bI8=E/(2*m**3*y*h*u)*(s.re(odd[3])-p*w/(E*u)*s.im(odd[2])-2*m*p/E*y*aI12)
checks=[aR2-ars[0],bR1-ars[3],aR12-ars[2],bR8-ars[5],aI2-ais[0],bI1-ais[3],aI12-ais[2],bI8-ais[5]]
assert all(s.simplify(c)==0 for c in checks)
print('PASS: four epsilon contractions, Euclidean ratios, and eight amplitude inversions.\nB1 imaginary uppercase conversion cancels eta exactly.')
