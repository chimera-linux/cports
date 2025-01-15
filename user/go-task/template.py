pkgname = "go-task"
pkgver = "3.40.1"
pkgrel = 0
build_style = "go"
make_build_args = [
    f"-ldflags=-X github.com/go-task/task/v3/internal/version.version=v{pkgver}",
    "./cmd/task",
]
hostmakedepends = ["go"]
pkgdesc = "Task runner / simpler Make alternative written in Go"
maintainer = "Mathijs Rietbergen <mathijs.rietbergen@proton.me>"
license = "MIT"
url = "https://taskfile.dev"
source = f"https://github.com/go-task/task/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "e80cdfa2afefa69238e5078960d50a8e703de1043740b277946629ca5f3bde85"
# conditionally disabled check
options = []

# test suite expects amd64
if self.profile().arch != "x86_64":
    options += ["!check"]


def post_install(self):
    self.install_license("LICENSE")

    self.install_completion("completion/fish/task.fish", "fish", "task")
    self.install_completion("completion/bash/task.bash", "bash", "task")
    self.install_completion("completion/zsh/_task", "zsh", "task")
