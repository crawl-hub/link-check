import logging


def should_ignore(page, link) -> bool:
    should_ignore_exts = [".json", ".pdf", ".zip"]
    for ext in should_ignore_exts:
        if link.endswith(ext):
            logging.warn("page: {}, {} link: {}".format(page, ext, link))
            return True

    shoule_ignore_schemes = ["mailto", "vscode"]

    for scheme in shoule_ignore_schemes:
        if link.startswith(scheme):
            logging.warn("page: {}, {} link: {}".format(page, scheme, link))
            return True
    return False
