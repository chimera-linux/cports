from pathlib import Path

def get_go_env(pkg):
    if not pkg.profile().goarch:
        pkg.error("Unknown architecture for golang")

    # * GOBIN is not suitable for crossbuild:
    #   "go: cannot install cross-compiled binaries when GOBIN is set"
    # * GOPATH must NOT contain a go.mod file, so cant' be '.'
    env = {
        "GOMODCACHE" : "/cbuild_cache/golang/pkg/mod",
        "GOARCH"     : pkg.profile().goarch,
        "GOPATH"     : f"{pkg.chroot_cwd}/{pkg.make_dir}"
    }
    return env

class Golang:
    def __init__(self, tmpl, jobs = None, env = {}, wrksrc = None):
        self.template = tmpl
        self.wrksrc = wrksrc
        self.env = env
        self.jobs = jobs

    def _invoke(
        self, command = None, args = [], jobs = None, offline = True,
        base_env = {}, env = {}, wrksrc = None
    ):

        if not command:
            self.template.error("Missing go command argument")

        # support only go.mod "mode" for now
        gomod = self.template.cwd / "go.mod"
        if not gomod.is_file():
            self.template.error(f"Missing file {gomod}")

        # need to recompute GOPATH with regular path (not chrooted),
        # since do_prepare phase is not chrooted
        mk_gomod = self.template.cwd / self.template.make_dir / "go.mod"
        if mk_gomod.is_file():
            self.template.error(
                f"GOPATH must not contain a go.mod file (make_dir is '{self.template.make_dir}')"
            )

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
            args = ["-p", str(jobs)] + args

        self.template.log(f"golang command: go {command} {' '.join(args)}")
        return self.template.do(
            "go", command, *self.template.configure_args, *args,
            env = renv, wrksrc = wrksrc, allow_network = not offline
        )

    def mod_download(self, args = [], env = {}, wrksrc = None):
        mode = self.template.go_mod_dl
        if mode == "off":
            self.template.log("skip modules download as requested")
            return

        vendor_dir = self.template.cwd / "vendor"
        if vendor_dir.is_dir() and mode != "mod":
            self.template.log("vendor/ is present, skip download of modules")
            return

        return self._invoke("mod", ["download"], 1, False, None, env, wrksrc)

    def build(self, args = [], jobs = None, env = {}, wrksrc = None):
        myargs = ['-x'] # increase go verbosity

        tags = self.template.go_build_tags
        if tags:
            myargs += ["-tags", (',').join(tags)]

        # imply that all generated binaries have the same PIE mode
        if self.template.has_hardening("pie") and \
           len(self.template.nopie_files) == 0 :
            myargs += ["-buildmode=pie"]

        ldflags = self.template.go_ldflags
        if ldflags:
            myargs += ["-ldflags", f"{(' ').join(ldflags)}"]
        if self.template.make_build_args:
            myargs += self.template.make_build_args
        myargs += args

        return self._invoke("install", myargs, jobs, True, None, env, wrksrc)

    def check(self):
        myargs = []

        tags = self.template.go_check_tags
        if tags:
            myargs += ["-tags", (',').join(tags)]
        if self.template.make_check_args:
            myargs += self.template.make_check_args
        return self._invoke("test", myargs)

    # rather basic installer
    def install(self):

        # XXX keep env in self.env, also for _invoke() code ?
        renv = get_go_env(self.template)
        renv.update(self.template.env)
        renv.update(self.env)

        # find either "native" files (bin/*)
        # or targeted arch file (bin/linux_<arch>/*)
        for f in Path(self.template.cwd / f"{self.template.make_dir}/bin").glob('**/*'):
            if f.is_file():
                self.template.install_bin(f)
