# techman_init (ver 1.7)
import sys, os
techman_config = {'min_ver': 1.9, 'path': '/tmp'.format(os.path.dirname(
    sys.argv[0])), 'link': 'https://resources.techmandev.com/libraries/techman.py'}  # Init params
try:
    sys.path.append('{}/'.format(techman_config['path']))
    import techman
    if not techman.library.is_compatible(techman_config['min_ver']):
        raise ModuleNotFoundError
except ModuleNotFoundError:
    try:
        import requests
        library = requests.get(techman_config['link']).text
        try:
            with open('{}/techman.py'.format(techman_config['path']), 'w') as file:
            	file.write(library)
        except:
            techman_config['path'] = '/tmp'
            with open('{}/techman.py'.format(techman_config['path']), 'w') as file:
            	file.write(library)
        sys.path.append('{}/'.format(techman_config['path']))
        import techman
    except ConnectionError as error:  # Internet error
        raise ConnectionError('{error}: \n\nPlease check your connection\n\nIf all else fails, you could download the techman.py file from {link} and save it to {path}'.format(
            link=techman_config['link'], error=error, path=techman_config['path']))
    except PermissionError as error:  # Write permission error
        raise PermissionError('{error}: \n\nPlease confirm that you have permission to write to this directory\n\nIf all else fails, you could download the techman.py file from {link} and save it to {path}'.format(
            link=techman_config['link'], error=error, path=techman_config['path']))
    # requests library missing (most likely) or library import error
    except ModuleNotFoundError as error:
        import subprocess
        try:
            try:
                subprocess.check_call([sys.executable, "-m", "pip", "install", 'requests'])
            except:
                try:
                    subprocess.check_call(["pip3", "install", 'requests'])
                except:
                    subprocess.check_call(["pip", "install", 'requests'])
        except:
            raise ModuleNotFoundError('{error}: \n\nPlease confirm that you have installed the requests library with \'pip3 install requests\'\n\nIf all else fails, you could download the techman.py file from {link} and save it to {path}'.format(
            link=techman_config['link'], error=error, path=techman_config['path']))

techman.quicksetup.is_first_open('jack', message='Hello')
techman.Packages.install('googletrans')
