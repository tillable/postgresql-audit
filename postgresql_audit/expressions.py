from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.sql import expression


class jsonb_merge(expression.FunctionElement):
    """
    Provides jsonb_merge as a SQLAlchemy FunctionElement.

    ::


        import sqlalchemy as sa
        from postgresql_audit import jsonb_merge


        data = {'key1': 1, 'key3': 4}
        merge_data = {'key1': 2, 'key2': 3}
        query = sa.select([jsonb_merge(data, merge_data)])
        session.execute(query).scalar()  # {'key1': 2, 'key2': 3, 'key3': 4}
    """
    type = JSONB()
    name = 'jsonb_merge'


@compiles(jsonb_merge)
def compile_jsonb_merge(element, compiler, **kw):
    arg1, arg2 = list(element.clauses)
    arg1.type = JSONB()
    arg2.type = JSONB()
    return 'jsonb_merge({0}, {1})'.format(
        compiler.process(arg1),
        compiler.process(arg2)
    )


class jsonb_change_key_name(expression.FunctionElement):
    """
    Provides jsonb_change_key_name as a SQLAlchemy FunctionElement.

    ::


        import sqlalchemy as sa
        from postgresql_audit import jsonb_change_key_name


        data = {'key1': 1, 'key3': 4}
        query = sa.select([jsonb_merge(data, 'key1', 'key2')])
        session.execute(query).scalar()  # {'key2': 1, 'key3': 4}
    """
    type = JSONB()
    name = 'jsonb_change_key_name'


@compiles(jsonb_change_key_name)
def compile_jsonb_change_key_name(element, compiler, **kw):
    arg1, arg2, arg3 = list(element.clauses)
    arg1.type = JSONB()
    return 'jsonb_change_key_name({0}, {1}, {2})'.format(
        compiler.process(arg1),
        compiler.process(arg2),
        compiler.process(arg3)
    )
