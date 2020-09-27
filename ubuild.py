import subprocess
# this is a uranium.py file
# it requires at the minimum a function
# main that accepts a parameter build.
def main(build):
    # you can change the index urls as desired.
    # packages are installed using the packages.install method.
    build.packages.install("py.test")
    # once an egg is installed, you can run arbitrary scripts installed
    # into the sandbox:
    return subprocess.call(["py.test", "mytests"] + build.options.args)