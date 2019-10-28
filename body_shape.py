
from sys import argv

script, shoulder, breast, waist, hips, ratio = argv
shoulder, breast, waist, hips = int(shoulder), int(breast), int(waist), int(hips)
ratio = float(ratio)

waist_over_others=0.75
besides_waist_ratio=0.06
A_breast_over_hips=0.95
T_breast_over_hips=1.05
lower_card=0.4
upper_card=0.5

body_shape=0
ratio=0

if 1-besides_waist_ratio<shoulder/breast<1+besides_waist_ratio and 1-besides_waist_ratio<hips/shoulder<1+besides_waist_ratio and 1-besides_waist_ratio<breast/hips<1+besides_waist_ratio and waist/breast <waist_over_others and waist/shoulder<waist_over_others and waist/hips < waist_over_others: 
    body_shape=1
if 1-besides_waist_ratio<shoulder/breast<1+besides_waist_ratio and 1-besides_waist_ratio<hips/shoulder<1+besides_waist_ratio and 1-besides_waist_ratio<breast/hips<1+besides_waist_ratio and 1>waist/breast >waist_over_others and 1>waist/shoulder>waist_over_others and 1>waist/hips > waist_over_others: 
    body_shape=2
if waist>=hips: 
    body_shape=3
    
if shoulder/hips<=1 or breast/hips<A_breast_over_hips:
    body_shape=1+body_shape
if shoulder/hips>=1 or breast/hips>T_breast_over_hips:
    body_shape=5+body_shape
    
if ratio<=lower_card: 
    ratio=1
if lower_card<ratio<upper_card: 
    ratio=2
if ratio>=upper_card: 
    ratio=3
print(body_shape,ratio)
