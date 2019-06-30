import typing

ScopeDeclaration = typing.Tuple[str, str]

DEFAULT_ACTIONS = ("read", "create", "updated", "delete")


def get_all_scopes(opts: typing.Any) -> typing.List[ScopeDeclaration]:
    return [*get_builtin_scopes(opts), *get_custom_scopes(opts)]


def get_builtin_scopes(opts: typing.Any) -> typing.List[ScopeDeclaration]:
    return [
        (action, "Can {} {}".format(action, opts.verbose_name_raw))
        for action in DEFAULT_ACTIONS
    ]


def get_custom_scopes(opts: typing.Any) -> typing.List[ScopeDeclaration]:
    return getattr(opts, "api_key_scopes", [])
