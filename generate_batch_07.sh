#!/usr/bin/env bash
set -e

# Экспорт путей для работы с pixverse CLI
export PATH="/opt/homebrew/bin:/usr/local/bin:$HOME/.npm-global/bin:$PATH"

OUTPUT_DIR="./rendered_batch_07"
mkdir -p "$OUTPUT_DIR"

echo "========================================================"
echo "🎬 Запуск пакетной генерации BATCH 07 (SHOT_031 — SHOT_035)"
echo "⚙️ Модель: PixVerse V6 | 720p | 5 сек | Без аудио (--no-audio)"
echo "========================================================"

declare -A PROMPTS=(
  ["SHOT_031"]="Slow cinematic rack focus from David's open trembling palms up to his face as he exhales in deep relief. Morning wind gently sways his hair, golden sunlight warming his skin, stable human anatomy, 24fps emotional realism."
  ["SHOT_032"]="Slow, respectful camera tilt-down from the glowing dawn clouds onto David kneeling in quiet prayer on the rock ledge. Mountain wind gently swaying his cloak hem, brilliant golden rim light outlining his silhouette, 24fps spiritual majesty."
  ["SHOT_033"]="Cinematic slow jib-up and pull-back camera motion revealing the vast majestic landscape of ancient Judea. Dramatic volumetric sunbeams slowly shifting across the misty valleys, clouds parting smoothly in the sky, 24fps epic scope."
  ["SHOT_034"]="Slow, steady tracking shot moving along the line of loyal Hebrew warriors as they step forward into unified formation beside David, morning wind fluttering their cloaks, spears catching the bright sun, 24fps filmic realism."
  ["SHOT_035"]="Static macro portrait on David's face as he slowly raises his gaze to the rising sun. A gentle morning wind rustles his hair, golden sunlight intensifies across his cheekbone, his chest rises with a slow, powerful breath of destiny, 24fps emotional majesty."
)

SHOT_LIST=("SHOT_031" "SHOT_032" "SHOT_033" "SHOT_034" "SHOT_035")

for shot in "${SHOT_LIST[@]}"; do
  prompt="${PROMPTS[$shot]}"
  
  # Поиск файла изображения (поддерживаются .jpeg, .jpg, .png)
  img_file=""
  for ext in "jpeg" "jpg" "png" "JPEG" "JPG" "PNG"; do
    if [ -f "${shot}.${ext}" ]; then
      img_file="${shot}.${ext}"
      break
    fi
  done

  if [ -z "$img_file" ]; then
    echo "⚠️ Файл изображения для ${shot} не найден в текущей папке. Пропуск..."
    continue
  fi

  echo "--------------------------------------------------------"
  echo "🚀 Генерация: ${shot} (файл: ${img_file})"
  echo "📝 Промпт: ${prompt}"
  
  # Отправка задачи в PixVerse CLI
  result=$(pixverse create video \
    --image "$img_file" \
    --prompt "$prompt" \
    --model v6 \
    --quality 720p \
    --duration 5 \
    --no-audio \
    --json)

  video_id=$(echo "$result" | jq -r '.video_id // empty')
  
  if [ -n "$video_id" ]; then
    echo "✅ Задача успешно выполнена! Video ID: ${video_id}"
    echo "📥 Скачивание видео в ${OUTPUT_DIR}/${shot}.mp4..."
    pixverse asset download "$video_id" --output-dir "$OUTPUT_DIR" --json || true
  else
    echo "❌ Ошибка генерации для ${shot}:"
    echo "$result"
  fi
done

echo "========================================================"
echo "🎉 Пакетная генерация завершена! Все видео сохранены в: ${OUTPUT_DIR}/"
echo "========================================================"
