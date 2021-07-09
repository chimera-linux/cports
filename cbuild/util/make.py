import shutil

_jobs = 1

def set_jobs(nj):
    global _jobs
    _jobs = nj

def jobs():
    return _jobs

class Make:
    def __init__(
        self, tmpl, jobs = None, command = None, env = {}, wrksrc = None
    ):
        self.template = tmpl
        self.command = command if command else tmpl.make_cmd
        self.wrksrc = wrksrc
        self.env = env

        if not jobs:
            self.jobs = _jobs
        else:
            self.jobs = jobs

        if tmpl.bootstrapping:
            # since usual Linux systems have make point to GNU make and bmake
            # point to BSD make, we need to make some adjustments for that:
            if self.command == "gmake":
                # if gmake was forced and does not exist, fall back to make
                if not shutil.which("gmake"):
                    self.command = "make"
            elif self.command == "make":
                # normal make means bmake for us; if it exists, use it
                if shutil.which("bmake"):
                    self.command = "bmake"

    def invoke(
        self, targets = [], args = [], jobs = None, env = {}, wrksrc = None
    ):
        renv = dict(self.env)
        renv.update(env)

        if not jobs:
            jobs = self.jobs

        if self.template.disable_parallel_build:
            jobs = 1

        argsbase = ["-j" + str(jobs)]

        if targets:
            if isinstance(targets, list):
                argsbase += targets
            else:
                argsbase.append(str(targets))

        argsbase += args

        return self.template.do(
            self.command, argsbase, build = True, env = renv,
            wrksrc = wrksrc if wrksrc else self.wrksrc
        )

    def build(self, args = [], jobs = None, env = {}, wrksrc = None):
        pkg = self.template
        return self.invoke(
            pkg.make_build_target, pkg.make_build_args + args,
            jobs, env, wrksrc
        )

    def install(
        self, args = [], jobs = None, env = {}, default_args = True,
        args_use_env = False, wrksrc = None
    ):
        pkg = self.template
        argsbase = []

        if default_args:
            if not args_use_env:
                argsbase.append("DESTDIR=" + str(pkg.chroot_destdir))
            else:
                renv = {"DESTDIR": str(pkg.chroot_destdir)}
                renv.update(env)
                env = renv

        argsbase += pkg.make_install_args
        argsbase += args

        return self.invoke(
            pkg.make_install_target, argsbase, jobs, env, wrksrc
        )
