# putting stuff in cflags/cxxflags has annoying warnings but it works around
# potentially broken build systems not accounting for ldflags
CBUILD_CFLAGS = ["-O2", "-pipe", "-rtlib=compiler-rt"]
CBUILD_CXXFLAGS = CBUILD_CFLAGS + ["-stdlib=libc++", "-unwindlib=libunwind"]
CBUILD_LDFLAGS = ["-fuse-ld=lld"]
