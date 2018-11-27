from . import bp

@bp.route('/')
def show():
    return '{"ret":"this is main page"}'