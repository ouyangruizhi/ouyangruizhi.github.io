# 欧阳瑞志个人科研主页

中英文双版本的科研主页，默认中文。内容依次为个人介绍与联系链接、教育经历、精选论文、公开项目、奖项与荣誉。

## 文件与维护

- `build.py`：生成中英文页面，个人介绍及教育经历也在此修改。
- `profile-data.json`：3 篇论文、5 项公开竞赛、1 项专利与 10 项软著、14 条奖项与荣誉。
- `contact-links.html`：ORCID、GitHub、Kaggle、Email 图标与链接。
- `dist/`：可以直接托管的网站；中文首页为 `index.html`，英文页为 `en/index.html`。
- `dist/assets/`：生活照、3 张论文原图与网站图标。
- `.github/workflows/pages.yml`：推送 main 分支后自动生成双语页面并发布 GitHub Pages。
- `.openai/`：旧 Sites 配置，已加入 Git 忽略规则，不用于 GitHub Pages。
- `.git/`：网站源码版本记录，保留用于更新发布。

修改内容后在此目录运行 `python3 build.py` 检查页面，推送到 GitHub 的 main 分支后自动发布。仅调整样式或交互时可直接修改 `dist/style.css`、`dist/script.js`。

本机预览：`python3 -m http.server 8765 --bind 127.0.0.1 --directory dist`，浏览器打开 http://127.0.0.1:8765/。

## 页面规则

竞赛默认显示最新两项，其他项目可展开。专利与软著固定先专利、后软著，同类先按署名顺序，再按日期从新到旧。中文“发明专利公开”类型保持单行。

荣誉默认先按年份从新到旧，再按级别从高到低；年份与级别表头分别切换排序方向，两个方向同时保留。英文级别与角色允许换行，年份列居中。

论文标题及期刊名保留英文，期刊名斜体、DOI 可见。航空发动机配图为原文 Figure 5，医药供应链为 Figure 1，五大湖为 Figure 5，图片无链接及下方说明。原图来源和许可记录见内容数据。

## 内容来源

个人信息、教育、荣誉与署名顺序来自用户确认的信息；论文信息来自 ORCID、出版方与原文；公开竞赛来自 GitHub、Kaggle。软著名称、日期与登记号已核对用户本地证书。网站不包含原始简历、论文 PDF、软著证书和其他附带文件。

## GitHub Pages 首次上线

目标为用户主页仓库 `ouyangruizhi.github.io`。迁移前需确认该仓库是否已存在，不覆盖其他网站。仓库 Settings → Pages → Source 选择 GitHub Actions，推送源码后等待 Publish research homepage 工作流成功。只发布 dist 文件夹；原始 PDF、旧 Sites 配置及其他本地文件不进入网页资源。
