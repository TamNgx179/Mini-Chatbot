FROM python:3.13-slim

# Keep container output immediate and avoid Python cache files.
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

WORKDIR /app

# Run the job as a non-root application user.
RUN addgroup --system app && adduser --system --ingroup app app

COPY requirements.txt ./
RUN python -m pip install --upgrade pip && \
    python -m pip install -r requirements.txt

# Copy only runtime code plus the legacy corpus used for first-run bootstrap.
COPY --chown=app:app main.py ./
COPY --chown=app:app src ./src
COPY --chown=app:app data/markdown ./data/markdown

RUN mkdir -p data/markdown data/state artifacts/run_reports && \
    chown -R app:app data artifacts

USER app

# One container invocation performs one sync and then exits.
ENTRYPOINT ["python", "main.py"]
CMD ["--all"]
