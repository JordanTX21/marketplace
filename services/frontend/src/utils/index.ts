/**
 * Función sleep que espera una cantidad específica de milisegundos.
 * @param ms - Número de milisegundos a esperar.
 * @returns Una promesa que se resuelve después de la cantidad especificada de milisegundos.
 */
export const sleep = (ms: number): Promise<void> => {
  return new Promise((resolve) => setTimeout(resolve, ms))
}