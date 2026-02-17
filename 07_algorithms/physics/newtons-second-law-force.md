# Newton's second law force calculation Python

Newton's second law (F=m⋅aF=m⋅a) calculates force from mass and acceleration, or vice versa, in classical mechanics.

## Simple Force Calculator

This basic code computes force, then uses it to update acceleration and motion—no libraries, pure arithmetic.

```
python# Newton's 2nd Law: Force calculation and motion (no libraries)
m = 5.0    # mass kg
a = 2.0    # acceleration m/s²

F = m * a  # Force in Newtons
print(f"Force: {F:.1f} N")

# Simulate motion with constant force
v = 0.0    # initial velocity
x = 0.0    # position
dt = 0.1   # time step
t_max = 2.0

t = 0.0
while t < t_max:
    print(f"t={t:.1f}, x={x:.1f}, v={v:.1f}, F={F:.1f}")
    
    a = F / m      # acceleration from F=ma
    v += a * dt    # update velocity
    x += v * dt    # update position
    t += dt
```

Outputs show force 10.0 N driving steady speedup. Reverse by solving a=F/ma=F/m or m=F/am=F/a. Great for pushes, pulls, or gravity (F=m⋅gF=m⋅g).
