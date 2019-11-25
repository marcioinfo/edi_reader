# Instruções Docker mongodb

Imagem:

```
docker pull tutum/mongodb
```


Criacao de volume

```
docker volume create mongodbdata
```

Para verificar local físico que foi criado o volume
```
docker volume inspect mongodbdata
```

Criar container sem autenticacao

``` 
docker run -d -p 27017:27017 -p 28017:28017 -e AUTH=no tutum/mongodb

```