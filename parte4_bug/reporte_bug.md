# Reporte de bug: La cantidad del carrito vuelve a 1 al girar la pantalla del teléfono celular. 

## Título 
Sobr el carrito de compras. La cantidad de un producto se reinicia a 1 al rotar la pantalla en Android 13 de la marca Samsung.

## Entorno
| Campo | Valor |
|---|---|
| Dispositivo | Samsung (modelo exacto por confirmar) |
| Sistema operativo | Android 13 |
| Versión de la app | Pendiente de confirmar |
| Origen | Reporte de usuario |

## Precondiciones 
- El usuario inció sesión en ShopGo. 
- El usuario tiene activada la rotación automática de pantalla en su teléfono. 

## Pasos para reproducirlo
1. Abrir el ShopGo con el teléfono en posición en vertical.
2. Agregar una camisa al carrito de compras. 
3. En el carrito, cambiar la cantidad de unidades de compra a 3. 
4. Verificar que la cantidad de unidades se muestre correctamente. 
5. Girar el teléfono horizontalmente. 

## Resultafo esperado
La cantidad se mantiene a 3 después de girarlo, y los datos de la orden de compra no cambian. 

## Resultado actual 
La cantidad vuelve a 1 después de rotar. 

## Severidad: Media 
La app no se cierra y el usuario puede corregir la cantidad. Pero se pueden perder datos sin aviso. 

## Prioridad: Alta 
Afecta al flujo de la compra, el usuario podría pagar menos unidades de las que verdaderamete desea comprar. Impacta directamente a las ventas y totales. 

## Evidencia que adjuntaría
- Video de la pantalla que muestre la rotación del dispositivo, y como cambia la cantidad antes y después de hacerlo. 
- Capturas del carrito con cantidad 3, y cantidad 1. 
- Logs del dispositivo durante la rotación. 

## Preguntas abiertas posibles
- ¿Qué modelo de Samsung y que versión de la app se está usando? 
- ¿Sucede con todos los productos, o solo con ese en específico? 
- ¿Pasa en otros dispositivos Android, o en otras versiones de SO movil? 
- ¿Pasa siempre que se gira la pantalla o solo en ocasiones? 