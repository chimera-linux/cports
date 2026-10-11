class Make:
    def __init__(self, tmpl, jobs=None, command=None, env=None, wrksrc=None):
        self.template = tmpl
        self.command = command or tmpl.make_cmd
        self.wrksrc = wrksrc
        self.env = env or {}
        self.jobs = jobs

    def _invoke(
        self, targets, args, jobs, base_env, env, wrksrc, ewrapper, wrapper
    ):
        renv = dict(self.template.make_env)
        if base_env:
            renv.update(base_env)
        renv.update(self.env)
        if env:
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

        if args:
            argsbase += args

        if not wrksrc:
            wrksrc = self.wrksrc
        if not wrksrc:
            wrksrc = self.template.make_dir

        return self.template.do(
            *(wrapper or []),
            *(ewrapper or []),
            *self.template.make_wrapper,
            self.command,
            *argsbase,
            env=renv,
            wrksrc=wrksrc,
        )

    def invoke(
        self,
        targets=None,
        args=None,
        jobs=None,
        env=None,
        wrksrc=None,
        wrapper=None,
    ):
        return self._invoke(
            targets, args, jobs, None, env, wrksrc, None, wrapper
        )

    def build(self, args=None, jobs=None, env=None, wrksrc=None, wrapper=None):
        pkg = self.template
        return self._invoke(
            pkg.make_build_target,
            pkg.make_build_args + (args or []),
            jobs,
            pkg.make_build_env,
            env,
            wrksrc,
            self.template.make_build_wrapper,
            wrapper,
        )

    def install(
        self,
        args=None,
        jobs=None,
        env=None,
        default_args=True,
        args_use_env=False,
        wrksrc=None,
        wrapper=None,
    ):
        pkg = self.template
        argsbase = []

        if default_args:
            if self.command == "ninja":
                args_use_env = True
            if not args_use_env:
                argsbase.append("DESTDIR=" + str(pkg.chroot_destdir))
            else:
                renv = {"DESTDIR": str(pkg.chroot_destdir)}
                renv.update(env)
                env = renv

        argsbase += pkg.make_install_args
        if args:
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

    def check(self, args=None, jobs=None, env=None, wrksrc=None, wrapper=None):
        pkg = self.template
        return self._invoke(
            pkg.make_check_target,
            pkg.make_check_args + (args or []),
            jobs,
            pkg.make_check_env,
            env,
            wrksrc,
            self.template.make_check_wrapper,
            wrapper,
        )
