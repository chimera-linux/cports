import shutil
import subprocess


def patch(pkg, patch_list, wrksrc=None, apply_args=[], stamp=False):
    if len(patch_list) == 0:
        return

    # first init a git repository, apply won't work without it
    if subprocess.run(["git", "init", "-q"], cwd=pkg.srcdir).returncode != 0:
        pkg.error("failed to initialize repository in source location")

    if (
        subprocess.run(
            ["git", "config", "--local", "gc.auto", "0"], cwd=pkg.srcdir
        ).returncode
        != 0
    ):
        pkg.error("failed setting initial git repository config")

    # now apply everything in a batch
    srcmd = [
        "env",
        "HOME=/dev/null",
        "git",
        "apply",
        "--whitespace=nowarn",
        *apply_args,
    ]

    def _apply(p):
        if subprocess.run([*srcmd, p], cwd=pkg.srcdir).returncode != 0:
            pkg.error(f"failed to apply '{p.name}'")

    for p in patch_list:
        pkg.log(f"patching: {p.name}")
        if stamp:
            with pkg.stamp(f"patch_{p.name}") as s:
                s.check()
                _apply(p)
        else:
            _apply(p)

    # now remove the repo so we don't give build systems ideas
    shutil.rmtree(pkg.srcdir / ".git")
