pkgname = "go-task"
pkgver = "3.43.2"
pkgrel = 3
build_style = "go"
make_build_args = [
    "./cmd/task",
]
hostmakedepends = ["go"]
pkgdesc = "Task runner / simpler Make alternative written in Go"
license = "MIT"
url = "https://taskfile.dev"
source = f"https://github.com/go-task/task/archive/refs/tags/v{pkgver}.tar.gz"
sha256 = "41ed911af61d582e2824e2ee6ac8b1a845968b09ed188e79846557226aa96bed"
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
