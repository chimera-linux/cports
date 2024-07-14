from pathlib import Path


def get_go_env(pkg):
    if not pkg.profile().goarch:
        pkg.error("unknown architecture for golang")

    env = {
        "GOMODCACHE": "/cbuild_cache/golang/pkg/mod",
        "GOARCH": pkg.profile().goarch,
        "CGO_CFLAGS": pkg.get_cflags(shell=True),
        "CGO_CXXFLAGS": pkg.get_cxxflags(shell=True),
        "CGO_LDFLAGS": pkg.get_ldflags(shell=True),
    }
    if env["GOARCH"] == "arm":
        if not pkg.profile().goarm:
            pkg.error("GOARCH is arm without matching GOARM")
        env["GOARM"] = pkg.profile().goarm

    return env


class Golang:
    def __init__(self, tmpl, jobs=None, env={}, wrksrc=None):
        self.template = tmpl
        self.wrksrc = wrksrc
        self.env = env
        self.jobs = jobs

    def _invoke(
        self,
        command=None,
        args=[],
        jobs=None,
        offline=True,
        base_env={},
        env={},
        wrksrc=None,
    ):
        if not command:
            self.template.error("golang: missing go command argument")

        # support only go.mod "mode" for now
        gomod = self.template.cwd / "go.mod"

        if not gomod.is_file():
            self.template.error(f"golang: missing file {gomod}")

        renv = get_go_env(self.template)
        renv.update(self.template.env)

        if base_env:
            renv.update(base_env)

        renv.update(self.env)
        renv.update(env)

        if not jobs:
            jobs = self.jobs
        if not jobs:
            jobs = self.template.make_jobs

        if command != "mod":
            args = ["-p", str(jobs), *args]

        self.template.log(f"golang: go {command} {' '.join(args)}")

        return self.template.do(
            "go",
            command,
            *self.template.configure_args,
            *args,
            env=renv,
            wrksrc=wrksrc,
            allow_network=not offline,
        )

    def mod_download(self, args=[], env={}, wrksrc=None):
        mode = self.template.go_mod_dl

        if mode == "off":
            self.template.log("golang: skip modules download as requested")
            return

        vendor_dir = self.template.cwd / "vendor"

        if vendor_dir.is_dir() and mode != "mod":
            self.template.log(
                "golang: vendor/ is present, skip download of modules"
            )
            return

        return self._invoke("mod", ["download"], 1, False, None, env, wrksrc)

    def build(self, args=[], jobs=None, env={}, wrksrc=None):
        myargs = ["-v", "-trimpath"]  # increase go verbosity, fix repro builds

        tags = self.template.go_build_tags

        if tags:
            myargs += ["-tags", (",").join(tags)]

        tmpl = self.template
        myargs += ["-o", str(tmpl.chroot_cwd / tmpl.make_dir) + "/"]

        if self.template.make_build_args:
            myargs += self.template.make_build_args

        myargs += args

        return self._invoke("build", myargs, jobs, True, None, env, wrksrc)

    def check(self):
        myargs = []

        tags = self.template.go_check_tags

        if tags:
            myargs += ["-tags", (",").join(tags)]

        if self.template.make_check_args:
            myargs += self.template.make_check_args
        else:
            myargs += ["./..."]

        return self._invoke("test", myargs)

    # rather basic installer
    def install(self):
        # XXX keep env in self.env, also for _invoke() code ?
        renv = get_go_env(self.template)
        renv.update(self.template.env)
        renv.update(self.env)

        # find either "native" files (bin/*)
        # or targeted arch file (bin/linux_<arch>/*)
        for f in Path(self.template.cwd / self.template.make_dir).glob("**/*"):
            if f.is_file():
                self.template.install_bin(f)
