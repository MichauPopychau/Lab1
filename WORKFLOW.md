# CI/CD Workflow (Render + GitHub Actions)

## 1. CI (GitHub Actions)

**Wyzwalacze:**
- \`push\` do gałęzi \`main\`
- \`pull_request\` do gałęzi \`main\`

**Kroki:**
1. **Checkout repo**  
   ```yaml
   uses: actions/checkout@v3
   ```
2. **Setup Python**  
   ```yaml
   uses: actions/setup-python@v4
   with:
     python-version: '3.9'
   ```
3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
4. **Install coverage**  
   ```bash
   pip install coverage
   ```
5. **Run tests** (100% coverage)  
   ```bash
   coverage run -m unittest discover
   coverage report --fail-under=100
   ```
6. **Lint code** (flake8)  
   ```bash
   pip install flake8
   flake8 .
   ```

Plik konfiguracyjny: \`.github/workflows/ci.yml\`

---

## 2. CD (Render)

**Wyzwalacz:**
- \`push\` do gałęzi \`main\`

**Kroki:**
1. **Render Auto Deploy**  
   - automatyczne wykonanie \`pip install -r requirements.txt\`  
   - start aplikacji: \`gunicorn main:app\` lub \`python main.py\`
2. **Health check**  
   - Render ping: \`/health\` (kod \`200\`)
3. **Rollback**  
   - renderowe GUI: zakładka *Events* > przy wybranym deployu > **Rollback**

---

## 3. Environment Variables

- Konfiguracja w Render → **Settings** → **Environment**
- Przykładowa zmienna:
  ```text
  SECRET=super_secret
  ```

---

## 4. Podsumowanie

1. **push/pr** → CI (GitHub Actions)  
2. **push main** → CD (Render Auto Deploy)  
3. **Health check** → \`/health\`  
4. **Rollback** → GUI Render  
5. **Env vars** → GUI Render
