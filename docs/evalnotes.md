# Data Quest — Evaluation Notes

## ex0 — Command Quest (lists via `sys.argv`)

- `sys.argv` is a list of strings;
  `argv[0]` is the program name,
  `argv[1:]` the args.
- "Multiple ways to avoid re-printing the program name":
  - slicing `sys.argv[1:]`
  - iterate `sys.argv[1:]`

## The `__class__.__dict__` dispatch (ex3)

`playerbase_show` looks up the method by name:
`p.__class__.__dict__[f"show_{version}"]`.

- class's namespace *is* a dict;
  methods are just functions stored in it,
  so I can fetch one by name.
- `Cls.__dict__` is a **`mappingproxy`**
  — a *read-only view* over the class's underlying namespace dict.
  I only read it, so that's fine.
- **Bound vs unbound:**
  indexing `__dict__` returns the **raw function**, not a bound method
  — that's why I pass the instance explicitly (`method(p)` / `method(p, rest)`).
  `getattr(p, name)` would return an *already-bound* method,
  called as `method()` / `method(rest)`.
- **Limitation:**
  `__dict__` only holds methods defined **directly on that class**, not inherited ones.
  `getattr` walks the **MRO** and finds inherited ones too.
  Here all `show_*` methods live on `Player`, so it's fine — not a general dispatch.
- **One-liner:**
  *"Methods live in the class's namespace,
  exposed as a read-only mappingproxy over a dict;
  I index it by name to get the underlying function and pass `self` in manually.
  `getattr` is the bound-method equivalent that also respects inheritance."*
- Simpler alternatives if pushed:
  `getattr(p, name)(...)`,
  or an explicit `{"gotten": Player.show_gotten, ...}` table (most defensible).
