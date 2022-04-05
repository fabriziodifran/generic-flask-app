# Nombre del Feature/Fix/Refactor
## Descripción
Se agrega la lógica para crear productos luego de haber pasado por el pipeline de steps de enriquecimiento.
## Issues involucrados
N/A #
## Razonamiento
Se agrega una nueva clase para el producto a generarse y un método que genera el producto a partir de un producto candidato enriquecido. Se agrega tambien un metodo para obtener el titulo mediante un request a la API de titulos.
## Cómo reproducirlo
Mediante un post al endpoint /catalog-discovery/brainiac/enrichment
## Checks
- [x] Pasaron los test localmente
- [N/A] Si estoy consumiendo un nuevo recurso. ¿Lo agregué al Traffic Catalog?
- [x] Revisé mi propio PR?
- [x] El código está bien formateado?
- [x] Evalué que los cambios que realicé no tengan un efecto secundario
    - [x] Retrocompatibilidad
    - [x] Avisar de breaking changes a involucrados
- [N/A] Agregué los cambios en el Changelog?
- [x] Agregué documentación?
- [ ] Deployé en un ambiente de test, probé mi feature y el flujo general.

# :warning: Merge según branch
| Branch desde | Branch hacia | Merge commit | Squash and Merge
| --- | --- | --- |---
| release  | master | :white_check_mark: | :x:
| backport | develop | :white_check_mark: | :x:
| hotfix | master/release | :x: | :white_check_mark:
| fix | release | :x: | :white_check_mark:
| feature | develop | :x: | :white_check_mark: |
Collaps
