# Terminal y Línea de Comandos

## Descripción

Este proyecto documenta el flujo de trabajo técnico utilizando terminal y línea de comandos. Demuestra capacidades en gestión de entornos, automatización CLI y control de versiones.

## Entorno de Desarrollo

### Stack Tecnológico

- **WSL (Windows Subsystem for Linux)** - Ubuntu 22.04
- **Bash** - Shell principal
- **Git** - Control de versiones
- **Python CLI** - Scripts de automatización

### Configuración del Entorno

```bash
# Actualizar sistema
sudo apt update && sudo apt upgrade -y

# Instalar herramientas básicas
sudo apt install -y git curl wget build-essential

# Configurar Python
sudo apt install -y python3 python3-pip
python3 --version

# Crear entorno virtual
python3 -m venv venv
source venv/bin/activate
```

## Comandos Frecuentes

### Git Workflow

```bash
# Clonar repositorio
git clone https://github.com/CesaReveron/portafolio.git

# Crear branch para nueva feature
git checkout -b feature/nueva-funcionalidad

# Ver estado
git status

# Añadir cambios
git add .
git commit -m "feat: descripción del cambio"

# Push a remoto
git push origin feature/nueva-funcionalidad

# Merge a main
git checkout main
git merge feature/nueva-funcionalidad
```

### Python Scripts

```bash
# Ejecutar script Python
python3 script.py

# Instalar dependencias
pip install -r requirements.txt

# Generar dataset
python3 proyectos/01_eda/src/generate_data.py

# Limpiar y analizar datos
python3 proyectos/01_eda/src/data_cleaning.py
python3 proyectos/01_eda/src/analysis.py
```

### Navegación y Archivos

```bash
# Navegación
cd ~/proyectos/portafolio
ls -la
pwd

# Buscar archivos
find . -name "*.py"
grep -r "funcion" --include="*.py"

# Permisos
chmod +x script.sh
```

## Automatización con Scripts

### Script de Generación de Datos

```bash
#!/bin/bash
# generate_data.sh

echo "Generando dataset..."
cd proyectos/01_eda/src
python3 generate_data.py
echo "Dataset generado exitosamente"
```

### Script de Actualización

```bash
#!/bin/bash
# update_project.sh

echo "Actualizando repositorio..."
git pull origin main
echo "Instalando dependencias..."
pip install -r proyectos/01_eda/requirements.txt
echo "Actualización completada"
```

## Configuraciones Útiles

### Git Aliases

```bash
# Añadir a ~/.gitconfig
[alias]
    st = status
    co = checkout
    br = branch
    lg = log --oneline --graph --all
```

### Variables de Entorno

```bash
# Añadir a ~/.bashrc
export PYTHONPATH="${PYTHONPATH}:/home/user/proyectos"
export EDITOR="code --wait"
```

## Flujo de Trabajo Típico

1. **Inicio de sesión**
   ```bash
   wsl  # Entrar a WSL
   cd ~/proyectos/portafolio
   source venv/bin/activate
   ```

2. **Desarrollo**
   ```bash
   git checkout -b feature/nueva-funcionalidad
   # Editar archivos
   python3 script.py  # Probar cambios
   ```

3. **Commit**
   ```bash
   git add .
   git commit -m "feat: descripción"
   git push origin feature/nueva-funcionalidad
   ```

4. **Revisión y Merge**
   ```bash
   git checkout main
   git pull origin main
   git merge feature/nueva-funcionalidad
   ```

## Recursos

- [Git Documentation](https://git-scm.com/doc)
- [Bash Guide](https://www.gnu.org/software/bash/manual/)
- [Python CLI Tutorial](https://docs.python.org/3/library/argparse.html)

## Próximos Pasos

- [ ] Implementar scripts de deployment automatizado
- [ ] Configurar aliases personalizados
- [ ] Crear Makefile para tareas comunes
- [ ] Documentar troubleshooting de problemas comunes