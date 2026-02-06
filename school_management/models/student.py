from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SchoolStudent(models.Model):
    _name = "school.student"
    _description = "Student"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "name"

    # Basic Info
    name = fields.Char(string="Full Name", required=True, tracking=True)
    student_code = fields.Char(
        string="Student Code",
        readonly=True,
        copy=False,
        index=True,
        tracking=True,
    )
    partner_id = fields.Many2one(
        "res.partner",
        string="Contact",
        ondelete="restrict",
        help="Linked partner for address, phone, email."
    )
    relation = fields.Selection(
        [("father", "Father"), ("mother", "Mother"), ("guardian", "Guardian")],
        string="Relation to Contact",
        tracking=True,
        help="Relationship between student and selected contact.",
    )
    academic_year_id = fields.Many2one(
        "school.academic.year",
        string="Academic Year",
        tracking=True
    )

    # Demographics
    gender = fields.Selection(
        [("male", "Male"), ("female", "Female"), ("other", "Other")],
        string="Gender",
        tracking=True,
    )
    dob = fields.Date(string="Date of Birth")
    age = fields.Integer(
        string="Age",
        compute="_compute_age",
        store=True,
        readonly=True,
    )
    photo = fields.Binary(string="Photo", attachment=True)

    # Guardian(s)
    guardian_ids = fields.Many2many(
        "school.guardian",
        "student_guardian_rel",
        "student_id",
        "guardian_id",
        string="Guardians",
    )

    # Other Info
    notes = fields.Text(string="Notes")

    # State Management
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("enrolled", "Enrolled"),
            ("alumni", "Alumni"),
            ("inactive", "Inactive"),
        ],
        default="draft",
        tracking=True,
    )
    active = fields.Boolean(default=True)

    # Constraints
    _sql_constraints = [
        ("student_code_unique", "unique(student_code)", "Student Code must be unique."),
    ]

    # Compute Age
    @api.depends("dob")
    def _compute_age(self):
        """Compute student's age from date of birth."""
        today = fields.Date.today()
        for rec in self:
            if rec.dob:
                rec.age = (
                    today.year
                    - rec.dob.year
                    - ((today.month, today.day) < (rec.dob.month, rec.dob.day))
                )
            else:
                rec.age = 0

    # Auto-generate Student Code
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get("student_code"):
                vals["student_code"] = (
                    self.env["ir.sequence"].next_by_code("school.student") or _("New")
                )
        return super().create(vals_list)

    # State actions
    def action_enroll(self):
        """Mark student as enrolled."""
        self.write({"state": "enrolled"})

    def action_set_alumni(self):
        """Mark student as alumni."""
        self.write({"state": "alumni"})
