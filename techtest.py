try:
    import techman
except ModuleNotFoundError:
    import sys, subprocess
    # implement pip as a subprocess:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '<packagename>'])

print(dir(techman))
techman.quicksetup.is_first_open('jack', message='Hello')
#techman.install('googletrans')
