# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint('news', __name__)
from . import view