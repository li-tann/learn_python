import pygmt
grid = pygmt.datasets.load_earth_relief(resolution="05m", region=[-108, -103, 35, 40])

fig = pygmt.Figure()
fig.grdview(
    grid=grid,
    perspective=[-130, 30],  # 设置 3D 视角
    frame=["xaf", "yaf", "WSnE"],
    projection="M15c",
    zsize="1.5c",
    surftype="s",
    cmap="geo",  # 设置 CPT
    plane="1000+ggrey",  # 设置平面高度 1000m，地表下填充灰色
    contourpen="0.1p",  # 设置等高线样式
)
fig.colorbar(perspective=True, frame=["a500", "x+lElevation", "y+lm"])  # 设置 perspective 选项让 colorbar 与图片角度一致
fig.show()