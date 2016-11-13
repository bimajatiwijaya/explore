import pytz
from openerp import SUPERUSER_ID
from datetime import datetime, timedelta
from openerp import models, fields, api, _
from openerp.tools import float_is_zero
from openerp.exceptions import UserError

class purchase_order(models.Model):
    _inherit = "purchase.order"
    
    @api.model
    def _get_time(self):
        now = datetime.now().date()
        return now

    date_create_nd = fields.Datetime('Tanggal : ', default=_get_time)
