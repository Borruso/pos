import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo-addons-oca-pos",
    description="Meta package for oca-pos Odoo addons",
    version=version,
    install_requires=[
        'odoo-addon-pos_customer_comment>=16.0dev,<16.1dev',
        'odoo-addon-pos_default_partner>=16.0dev,<16.1dev',
        'odoo-addon-pos_escpos_status>=16.0dev,<16.1dev',
        'odoo-addon-pos_order_remove_line>=16.0dev,<16.1dev',
        'odoo-addon-pos_order_reorder>=16.0dev,<16.1dev',
        'odoo-addon-pos_order_to_sale_order>=16.0dev,<16.1dev',
        'odoo-addon-pos_payment_terminal>=16.0dev,<16.1dev',
        'odoo-addon-pos_product_display_default_code>=16.0dev,<16.1dev',
        'odoo-addon-pos_product_quick_info>=16.0dev,<16.1dev',
        'odoo-addon-pos_receipt_hide_price>=16.0dev,<16.1dev',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 16.0',
    ]
)
