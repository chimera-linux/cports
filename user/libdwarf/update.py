# don't fetch versions from prevanders.net, only tags
url = (
    "https://github.com/davea42/libdwarf-code/info/refs?service=git-upload-pack"
)
pattern = r"refs/tags/v([\d.]+)"
