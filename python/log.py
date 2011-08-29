import re
import logging
from colorama import Fore, Back, Style

# global LOG
LOG = logging.getLogger('modelp')
handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
LOG.addHandler(handler)
LOG.setLevel(logging.DEBUG)

def debug(msg):
    LOG.debug(colorize(msg))

def info(msg):
    LOG.info(colorize(msg))

def warning(msg):
    LOG.warning(colorize(msg))

def error(msg):
    LOG.error(colorize(msg))

def critical(msg):
    LOG.critical(colorize(msg))
    
def colorize(msg):
    params = {
        r'\-\-\->'        : '~FB~SB--->~FW',
        r'\*\*\*>'        : '~FB~SB~BB--->~BT~FW',
        r'\['             : '~SB~FB[~SN~FM',
        r'\*\]'           : '~SN~FR*]',
        r'\]'             : '~FB~SB]~FW~SN',
    }
    colors = {
        '~SB' : Style.BRIGHT,
        '~SN' : Style.NORMAL,
        '~SK' : Style.BLINK,
        '~SU' : Style.UNDERLINE,
        '~ST' : Style.RESET_ALL,
        '~FK': Fore.BLACK,
        '~FR': Fore.RED,
        '~FG': Fore.GREEN,
        '~FY': Fore.YELLOW,
        '~FB': Fore.BLUE,
        '~FM': Fore.MAGENTA,
        '~FC': Fore.CYAN,
        '~FW': Fore.WHITE,
        '~FT': Fore.RESET,
        '~BK': Back.BLACK,
        '~BR': Back.RED,
        '~BG': Back.GREEN,
        '~BY': Back.YELLOW,
        '~BB': Back.BLUE,
        '~BM': Back.MAGENTA,
        '~BC': Back.CYAN,
        '~BW': Back.WHITE,
        '~BT': Back.RESET,
    }
    for k, v in params.items():
        msg = re.sub(k, v, msg)
    msg = msg + '~ST~FW~BT'
    msg = re.sub(r'(~[A-Z]{2})', r'%(\1)s', msg)
    try:
        msg = msg % colors
    except (TypeError, ValueError, KeyError):
        pass

    return msg + Fore.RESET

if __name__ == '__main__':
    print 
    debug('~SU[~FRModel A]~ST: ~FMxxxxxxxx ~FT')
    info('~SU[~FRModel A]~ST: ~FGxxxxxxxx ~FT')
    warning('~SU[~FRModel A]~ST: ~FYxxxxxxxx ~FT')
    error('~SU[~FRModel A]~ST: ~FRxxxxxxxx ~FT')
    critical('~SU[~FRModel A]~ST: ~BW~FKxxxxxxxx ~BT')
    print 
