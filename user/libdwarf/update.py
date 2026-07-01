# template url points to prevanders.net, which pollutes the check with
# legacy date tags (YYYYMMDD) and an old 0.x series. Restrict to GitHub tags.
url = "https://github.com/davea42/libdwarf-code/tags"
pattern = r"/tag/v([\d.]+)"
