import shutil


class Make:
    def __init__(self, tmpl, jobs=None, command=None, env={}, wrksrc=None):
        self.template = tmpl
        self.command = command
        self.wrksrc = wrksrc
        self.env = env
        self.jobs = jobs

    def get_command(self):
        if self.command:
            return self.command

        self.command = self.template.make_cmd

        if self.template.stage == 0:
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

        return self.command

    def _invoke(
        self, targets, args, jobs, base_env, env, wrksrc, ewrapper, wrapper
    ):
        renv = dict(self.template.make_env)
        if base_env:
            renv.update(base_env)
        renv.update(self.env)
        renv.update(env)

        if not jobs:
            jobs = self.jobs

        if not jobs:
            jobs = self.template.make_jobs

        argsbase = ["-j" + str(jobs)]

        if targets:
            if isinstance(targets, list):
                argsbase += targets
            else:
                argsbase.append(str(targets))

        argsbase += args

        if not wrksrc:
            wrksrc = self.wrksrc
        if not wrksrc:
            wrksrc = self.template.make_dir

        return self.template.do(
            *wrapper,
            *ewrapper,
            *self.template.make_wrapper,
            self.get_command(),
            *argsbase,
            env=renv,
            wrksrc=wrksrc,
        )

    def invoke(
        self, targets=[], args=[], jobs=None, env={}, wrksrc=None, wrapper=[]
    ):
        return self._invoke(targets, args, jobs, None, env, wrksrc, [], wrapper)

    def build(self, args=[], jobs=None, env={}, wrksrc=None, wrapper=[]):
        pkg = self.template
        return self._invoke(
            pkg.make_build_target,
            pkg.make_build_args + args,
            jobs,
            pkg.make_build_env,
            env,
            wrksrc,
            self.template.make_build_wrapper,
            wrapper,
        )

    def install(
        self,
        args=[],
        jobs=None,
        env={},
        default_args=True,
        args_use_env=False,
        wrksrc=None,
        wrapper=[],
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

        return self._invoke(
            pkg.make_install_target,
            argsbase,
            jobs,
            pkg.make_install_env,
            env,
            wrksrc,
            self.template.make_install_wrapper,
            wrapper,
        )

    def check(self, args=[], jobs=None, env={}, wrksrc=None, wrapper=[]):
        pkg = self.template
        return self._invoke(
            pkg.make_check_target,
            pkg.make_check_args + args,
            jobs,
            pkg.make_check_env,
            env,
            wrksrc,
            self.template.make_check_wrapper,
            wrapper,
        )
