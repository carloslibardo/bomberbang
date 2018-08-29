# bomberbang

A stupid project created by two stupid students.

## Project Structure

### screens

Where all the components who interact with the user view will be located.

### app

Where the components that interact with user actions will be located.

### assets

Where resources, like images, will be located.

### config

Location for configuration files.

### common

Common used items for different components.

### components

Components that are used in others components.

## Dependencies

Include here dependencies of node like this

### Example

Example dependencie module of node.

```
npm install -i example
```

## Running

With dependencies installed, run the command:

```
react-native run-android
```

for android.

## Notas para o Carlinhos

### Problema com NDK

Ir no android studio e selecionar na aba de opções do sdk a utilização de ndk, vai baixar dai e resolve seus problemas.

### Problemas com java

Baixar o jdk1.8 do site e descompactar em algum lugar do seu disco depois usar o comando:

```
export JAVA_HOME=localizacao_do_java
```

### Problemas envolvendo gradle

Adicionar na pasta dentro do diretório do arquivo android/gradle/wrapper no arquivo gradle-wrapper.properties:

```
distributionUrl=https\://services.gradle.org/distributions/gradle-4.4-all.zip
```
