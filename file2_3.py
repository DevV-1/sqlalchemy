#############sql query builder

import sqlite3
from pypika import Order, Query, Table, functions

def main():
    n_of_top_cistomers = int(input('enter number: '))

    invoice = Table("Invoice")
    customer = Table("Customer")
    # query = (
    #     Query.from_(invoice)
    #     .left_join(customer)
    #     .on(invoice.customer_id == customer.id)
    #     .groupby(customer.id, customer.fname)
    #     .orderby(functions.Sum(invoice.total), order = Order.desc)
    #     .limit(n_of_top_cistomers)
    #     .select{
    #         customer.id,
    #         customer.fname,
    #         functions.Sum(invoice.total).as_("total"),
    #     } 
    # )