# https://sagecell.sagemath.org/ -> 여기서 실행하는게 편할 것
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# 로렌츠 시스템의 미분 방정식
def lorenz_system(t, state, sigma, rho, beta):
    x, y, z = state
    dx_dt = sigma * (y - x)
    dy_dt = x * (rho - z) - y
    dz_dt = x * y - beta * z
    return [dx_dt, dy_dt, dz_dt]

# 초기 조건과 매개 변수 설정
initial_state = [1.0, 0.0, 0.0]
sigma = 10.0
rho = 28.0
beta = 8.0 / 3.0

# 시뮬레이션을 위한 시간 범위 설정
t_span = (0, 100)
t_eval = np.linspace(t_span[0], t_span[1], 10000)

# 미분 방정식을 풀어 시뮬레이션 실행
solution = solve_ivp(
    lorenz_system,
    t_span=t_span,
    y0=initial_state,
    args=(sigma, rho, beta),
    t_eval=t_eval,
)

# 시각화
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(solution.y[0], solution.y[1], solution.y[2], lw=0.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Lorenz Chaos')
plt.show()