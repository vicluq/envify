# Env Parser

A friendly enviroment variable parser to describe envs and parse them. This will make documenting environment variables easier.

## Basic Usage

Import the `config` function and provide a configuration `.yaml` or `.yml` file to it as bellow:

```yaml
envs:
    env_id:
        name: string
        description: string
        options: [value_type]
        required: true | false
        value_type: str | int | bool | float
```

example:

```yaml
envs:
  redis_url:
    name: 'REDIS_URL'
    description: "The redis database URL"
    options: ['redis://localhost:6379']
    required: true
    value_type: str
```

The `config` function returns a `dict` with the parsed envs converted to it's type.

### Env Properties

- `name`: it should be the same string as in your .env file
- `description`: a short description of what is it
- `options`: a list of the possible values the env can receive
    - If any different value is provided, it will issue an error
- `required`: if the env variable is required or not
- `value_type`: a string representing the convertion type of the env value
    - Currently supports: `str`, `int`, `bool` and `float`

## Multiple Environs

To use multiple environs, must set the `multi` key to `true` and you have to add them as top level after the `envs:` directive. We have three possible environs: `development`, `staging`, `production`.

```yaml
envs:
    multi: true
    active: 'development' | 'staging' | 'production' 
    development:
        # Normal env declaration
    staging:
        # Normal env declaration
    production:
        # Normal env declaration
```

In your `.env` (or wherever you put your envs), for each type of environ, the env must have the correct prefix:

- `DEV_` for `development`
- `STAG_` for `staging`
- `PROD_` for `production`

The loader will return a tuple: `(active, envs)` with the active environ and all of the parsed environs, respectively.

If no `active` is provided, it will return `(None, envs)`.

If you enable environs, you can't have misplaced envs outside of them to avoid possible security issues.

### Possible Errors

- If an environment is empty, it will issue a waring
- If a name different than the reserved ones for a eviron is giver, it will issue an error
    - _Custom environs are in progress!_
- If your not using environments and make use of the `active: true|false` directive, it will treat it as a env variable and issue a invalid env error
