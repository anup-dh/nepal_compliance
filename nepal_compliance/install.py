import frappe

# from nepal_compliance.custom_code.payroll.salary_structure import create_salary_structures
from nepal_compliance.custom_code.payroll.income_tax_slab import create_income_tax_slabs_for_all_companies
from nepal_compliance.custom_field import create_custom_fields
from nepal_compliance.custom_code.payroll.payroll_settings import modify_email_salary_slip_default
def install():
    create_custom_fields()
    create_income_tax_slabs_for_all_companies()
    modify_email_salary_slip_default()
    # create_salary_structures()

    