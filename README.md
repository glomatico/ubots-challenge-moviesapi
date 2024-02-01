# ubots-challenge-moviesapi

Uma API RESTful que retorna informações e avaliações de filmes, desenvolvida para o desafio técnico do processo seletivo para vaga de desenvolvedor na Ubots.

A API foi desenvolvida em Python, utilizando o framework FastAPI em conjunto com a biblioteca SQLModel para a integração com o banco de dados.

## Rotas

### [POST]/create/movie

- Summary  
Create Movie

#### RequestBody

- application/json

```ts
{
  id?: Partial(integer) & Partial(null)
  title: string
  synopsis: string
  language: string
  rating: string
  release_date: string
  duration: string
}
```

#### Responses

- 200 Successful Response

`application/json`

```ts
{
  id?: Partial(integer) & Partial(null)
  title: string
  synopsis: string
  language: string
  rating: string
  release_date: string
  duration: string
}
```

- 422 Validation Error

`application/json`

```ts
{
  detail: {
    loc?: Partial(string) & Partial(integer)[]
    msg: string
    type: string
  }[]
}
```

***

### [POST]/create/review

- Summary  
Create Review

#### RequestBody

- application/json

```ts
{
  id?: Partial(integer) & Partial(null)
  stars: integer
  comment: string
  movie_id?: integer
}
```

#### Responses

- 200 Successful Response

`application/json`

```ts
{
  id?: Partial(integer) & Partial(null)
  stars: integer
  comment: string
  movie_id?: integer
}
```

- 422 Validation Error

`application/json`

```ts
{
  detail: {
    loc?: Partial(string) & Partial(integer)[]
    msg: string
    type: string
  }[]
}
```

***

### [POST]/delete/movie/{movie_id}

- Summary  
Delete Movie

#### Responses

- 200 Successful Response

`application/json`

```ts
{
}
```

- 422 Validation Error

`application/json`

```ts
{
  detail: {
    loc?: Partial(string) & Partial(integer)[]
    msg: string
    type: string
  }[]
}
```

***

### [POST]/delete/review/delete_by_review_id/{review_id}

- Summary  
Delete Review

#### Responses

- 200 Successful Response

`application/json`

```ts
{
}
```

- 422 Validation Error

`application/json`

```ts
{
  detail: {
    loc?: Partial(string) & Partial(integer)[]
    msg: string
    type: string
  }[]
}
```

***

### [POST]/delete/reviews/delete_by_movie_id/{movie_id}

- Summary  
Delete Reviews

#### Responses

- 200 Successful Response

`application/json`

```ts
{
}
```

- 422 Validation Error

`application/json`

```ts
{
  detail: {
    loc?: Partial(string) & Partial(integer)[]
    msg: string
    type: string
  }[]
}
```

***

### [GET]/get/movie/{movie_id}

- Summary  
Get Movie By Movie Id

#### Responses

- 200 Successful Response

`application/json`

```ts
{
  id?: Partial(integer) & Partial(null)
  title: string
  synopsis: string
  language: string
  rating: string
  release_date: string
  duration: string
}
```

- 422 Validation Error

`application/json`

```ts
{
  detail: {
    loc?: Partial(string) & Partial(integer)[]
    msg: string
    type: string
  }[]
}
```

***

### [GET]/get/movies

- Summary  
Get Movies

#### Responses

- 200 Successful Response

`application/json`

```ts
{
  id?: Partial(integer) & Partial(null)
  title: string
  synopsis: string
  language: string
  rating: string
  release_date: string
  duration: string
}[]
```

***

### [GET]/get/review/by_review_id/{review_id}

- Summary  
Get Review By Review Id

#### Responses

- 200 Successful Response

`application/json`

```ts
{
  id?: Partial(integer) & Partial(null)
  stars: integer
  comment: string
  movie_id?: integer
}
```

- 422 Validation Error

`application/json`

```ts
{
  detail: {
    loc?: Partial(string) & Partial(integer)[]
    msg: string
    type: string
  }[]
}
```

***

### [GET]/get/reviews/by_movie_id/{movie_id}

- Summary  
Get Reviews By Movie Id

#### Responses

- 200 Successful Response

`application/json`

```ts
{
  id?: Partial(integer) & Partial(null)
  stars: integer
  comment: string
  movie_id?: integer
}[]
```

- 422 Validation Error

`application/json`

```ts
{
  detail: {
    loc?: Partial(string) & Partial(integer)[]
    msg: string
    type: string
  }[]
}
```

***

### [GET]/get/reviews

- Summary  
Get Reviews

#### Responses

- 200 Successful Response

`application/json`

```ts
{
  id?: Partial(integer) & Partial(null)
  stars: integer
  comment: string
  movie_id?: integer
}[]
```

***

### [GET]/

- Summary  
Root

#### Responses

- 200 Successful Response

`application/json`

```ts
{}
```

***

### [POST]/update/movie

- Summary  
Update Movie

#### RequestBody

- application/json

```ts
{
  id?: Partial(integer) & Partial(null)
  title: string
  synopsis: string
  language: string
  rating: string
  release_date: string
  duration: string
}
```

#### Responses

- 200 Successful Response

`application/json`

```ts
{
  id?: Partial(integer) & Partial(null)
  title: string
  synopsis: string
  language: string
  rating: string
  release_date: string
  duration: string
}
```

- 422 Validation Error

`application/json`

```ts
{
  detail: {
    loc?: Partial(string) & Partial(integer)[]
    msg: string
    type: string
  }[]
}
```

***

### [POST]/update/review

- Summary  
Update Movie

#### RequestBody

- application/json

```ts
{
  id?: Partial(integer) & Partial(null)
  stars: integer
  comment: string
  movie_id?: integer
}
```

#### Responses

- 200 Successful Response

`application/json`

```ts
{
  id?: Partial(integer) & Partial(null)
  stars: integer
  comment: string
  movie_id?: integer
}
```

- 422 Validation Error

`application/json`

```ts
{
  detail: {
    loc?: Partial(string) & Partial(integer)[]
    msg: string
    type: string
  }[]
}
```

## References

### #/components/schemas/HTTPValidationError

```ts
{
  detail: {
    loc?: Partial(string) & Partial(integer)[]
    msg: string
    type: string
  }[]
}
```

### #/components/schemas/Movie

```ts
{
  id?: Partial(integer) & Partial(null)
  title: string
  synopsis: string
  language: string
  rating: string
  release_date: string
  duration: string
}
```

### #/components/schemas/Review

```ts
{
  id?: Partial(integer) & Partial(null)
  stars: integer
  comment: string
  movie_id?: integer
}
```

### #/components/schemas/ValidationError

```ts
{
  loc?: Partial(string) & Partial(integer)[]
  msg: string
  type: string
}
```