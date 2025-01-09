from cbuild.core import paths


def configure(
    pkg,
    build_dir,
    cmake_dir=None,
    extra_args=[],
    env={},
    generator=None,
    cross_build=None,
):
    if cmake_dir:
        cdir = pkg.chroot_cwd / cmake_dir
    else:
        cdir = pkg.chroot_cwd

    (pkg.cwd / build_dir).mkdir(parents=True, exist_ok=True)

    cargs = []

    if pkg.stage == 0:
        with open(pkg.cwd / build_dir / "bootstrap.cmake", "w") as infile:
            infile.write(
                f"""
SET(CMAKE_SYSTEM_NAME Linux)
SET(CMAKE_SYSTEM_VERSION 1)

SET(CMAKE_C_COMPILER   {pkg.get_tool("CC")})
SET(CMAKE_CXX_COMPILER {pkg.get_tool("CXX")})

SET(CMAKE_FIND_ROOT_PATH  "{paths.bldroot() / "usr"};{paths.bldroot()}")

SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
"""
            )
        cargs.append("-DCMAKE_TOOLCHAIN_FILE=bootstrap.cmake")
    elif pkg.profile().cross and cross_build is not False:
        # map known profiles to cmake arch
        match pkg.profile().arch:
            case (
                "aarch64"
                | "ppc64le"
                | "ppc64"
                | "ppc"
                | "x86_64"
                | "riscv64"
                | "armhf"
                | "armv7"
            ):
                cmake_cpu = pkg.profile().arch
            case _:
                pkg.error(f"unknown cmake architecture: {pkg.profile().arch}")

        sroot = pkg.profile().sysroot

        with open(pkg.cwd / build_dir / "cross.cmake", "w") as infile:
            infile.write(
                f"""
SET(CMAKE_SYSTEM_NAME Linux)
SET(CMAKE_SYSTEM_VERSION 1)

SET(CMAKE_C_COMPILER   {pkg.get_tool("CC")})
SET(CMAKE_CXX_COMPILER {pkg.get_tool("CXX")})
SET(CMAKE_C_COMPILER_TARGET {pkg.profile().triplet})
SET(CMAKE_CXX_COMPILER_TARGET {pkg.profile().triplet})
SET(CMAKE_ASM_COMPILER_TARGET {pkg.profile().triplet})
SET(CMAKE_CROSSCOMPILING TRUE)
SET(CMAKE_SYSROOT "{sroot}")

SET(CMAKE_SYSTEM_PROCESSOR {cmake_cpu})

SET(CMAKE_FIND_ROOT_PATH  "{sroot / "usr"};{sroot}")

SET(CMAKE_FIND_ROOT_PATH_MODE_PROGRAM NEVER)
SET(CMAKE_FIND_ROOT_PATH_MODE_LIBRARY ONLY)
SET(CMAKE_FIND_ROOT_PATH_MODE_INCLUDE ONLY)
"""
            )
        cargs.append("-DCMAKE_TOOLCHAIN_FILE=cross.cmake")

    # this is necessary for lto to work correctly
    if pkg.stage >= 2:
        cargs += [
            f"-DCMAKE_AR=/usr/bin/{pkg.get_tool('AR')}",
            f"-DCMAKE_NM=/usr/bin/{pkg.get_tool('NM')}",
            f"-DCMAKE_RANLIB=/usr/bin/{pkg.get_tool('RANLIB')}",
        ]

    # TODO: try put these args in a toolchain file like above even for native, if it
    # silences all the warnings about unused args and actually works
    pkg.do(
        "cmake",
        "-G",
        generator or "Ninja",
        *cargs,
        "-Wno-dev",
        f"-DCMAKE_AUTOGEN_PARALLEL={min(pkg.make_jobs, 2)}",
        "-DCMAKE_BUILD_TYPE=None",
        "-DCMAKE_INSTALL_PREFIX=/usr",
        "-DCMAKE_TLS_VERIFY=ON",
        "-DFETCHCONTENT_TRY_FIND_PACKAGE_MODE=ALWAYS",
        "-DFETCHCONTENT_FULLY_DISCONNECTED=ON",
        "-DCMAKE_INSTALL_SYSCONFDIR=/etc",
        "-DCMAKE_INSTALL_RUNSTATEDIR=/run",
        "-DCMAKE_INSTALL_LOCALSTATEDIR=/var",
        "-DCMAKE_INSTALL_LIBDIR=lib",
        "-DCMAKE_INSTALL_LIBEXECDIR=libexec",
        "-DCMAKE_INSTALL_SBINDIR=bin",
        "-DCMAKE_INSTALL_BINDIR=bin",
        "--fresh",
        *extra_args,
        cdir,
        wrksrc=build_dir,
        env=env,
    )


def build(pkg, build_dir, extra_args=[], env={}, wrapper=[]):
    pkg.do(
        *wrapper,
        "cmake",
        "--build",
        ".",
        "--parallel",
        str(pkg.make_jobs),
        *extra_args,
        wrksrc=build_dir,
        env=env,
    )


def install(pkg, build_dir, extra_args=[], env={}, wrapper=[]):
    renv = {"DESTDIR": str(pkg.chroot_destdir)}
    renv.update(env)

    pkg.do(
        *wrapper,
        "cmake",
        "--install",
        ".",
        *extra_args,
        wrksrc=build_dir,
        env=renv,
    )


def ctest(pkg, build_dir, extra_args=[], env={}, wrapper=[]):
    renv = {
        "CTEST_PARALLEL_LEVEL": str(pkg.make_jobs),
        "CTEST_OUTPUT_ON_FAILURE": "1",
    }
    renv.update(env)

    pkg.do(
        *wrapper,
        "ctest",
        *extra_args,
        wrksrc=build_dir,
        env=renv,
    )
