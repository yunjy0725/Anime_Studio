
import io
import base64
import tempfile
from pathlib import Path

import streamlit as st
from PIL import Image
from openai import OpenAI


# ==========================================
# STEP 1. 기본 설정
# ==========================================

st.set_page_config(
    page_title="Anime Studio",
    page_icon="🎨",
    layout="wide"
)

st.title("🎨 Anime Studio")
st.write("나만의 사진을 다양한 애니메이션 그림체로 변환해 보세요!")


# ==========================================
# STEP 2. OpenAI API 연결
# ==========================================

def get_openai_client():

    api_key = st.secrets.get("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OpenAI API 키를 찾을 수 없습니다. "
            ".streamlit/secrets.toml을 확인해 주세요."
        )

    return OpenAI(api_key=api_key)


# ==========================================
# STEP 3. 그림체별 프롬프트 설정
# ==========================================

STYLE_PROMPTS = {

    "디즈니풍": """
    Transform the person in the uploaded photo into
    a charming 3D animated family-film character.

    Use expressive eyes, appealing facial expressions,
    smooth 3D materials, warm cinematic lighting,
    and beautiful detailed rendering.

    Preserve the person's recognizable facial features,
    hairstyle, pose, clothing, and overall composition.

    Do not copy any existing copyrighted character.
    """,

    
    "픽사풍": """
    Transform the person into a highly distinctive,
    stylized 3D animated movie character.

    Emphasize:
    - Unique and expressive facial proportions.
    - Slightly exaggerated nose, cheeks and jaw shape.
    - Richly detailed skin and hair textures.
    - Sculpted 3D facial features with strong depth.
    - Warm studio lighting and cinematic rendering.
    - Playful personality and distinctive character design.

    Avoid the elegant fairytale princess look.
    Avoid generic Disney-like facial proportions.

    Preserve the person's identity, hairstyle,
    clothing, pose and overall composition.

    Do not copy any existing copyrighted character.
    """,

    "한국 웹툰풍": """
    Transform the person in the uploaded photo into
    a polished Korean webtoon character illustration.

    Use clean and elegant line art,
    refined facial features, smooth cel shading,
    beautiful color grading, and detailed illustration.

    Preserve the person's recognizable facial features,
    hairstyle, pose, clothing, and overall composition.
    """
}


# ==========================================
# STEP 4. OpenAI 이미지 변환 함수
# ==========================================

def convert_to_anime(image, style):

    client = get_openai_client()

    prompt = STYLE_PROMPTS[style]

    with tempfile.TemporaryDirectory() as temp_dir:

        temp_path = Path(temp_dir) / "input.png"

        # 원본 사진을 PNG로 저장
        image.convert("RGB").save(
            temp_path,
            format="PNG"
        )

        # OpenAI 이미지 편집 API 호출
        with open(temp_path, "rb") as image_file:

            response = client.images.edit(
                model="gpt-image-2.5-flare",
                image=image_file,
                prompt=prompt
            )

        # 변환된 이미지 데이터 가져오기
        image_base64 = response.data[0].b64_json

        image_bytes = base64.b64decode(image_base64)

        # 이미지 불러오기
        result_image = Image.open(
            io.BytesIO(image_bytes)
        ).convert("RGB")

        return result_image.copy()


# ==========================================
# STEP 5. 사진 업로드 및 촬영
# ==========================================

st.subheader("📷 사진 선택")

upload_col, camera_col = st.columns(2)

with upload_col:

    uploaded_image = st.file_uploader(
        "사진을 업로드하세요.",
        type=["jpg", "jpeg", "png"],
        key="image_upload"
    )

with camera_col:

    camera_image = st.camera_input(
        "카메라로 직접 촬영하세요."
    )


# 촬영 사진이 있으면 촬영 사진 우선 사용
selected_image = (
    camera_image
    if camera_image is not None
    else uploaded_image
)


# ==========================================
# STEP 6. 사진 미리보기
# ==========================================

if selected_image is not None:

    image = Image.open(
        selected_image
    ).convert("RGB")

    st.divider()

    st.subheader("🖼️ 원본 사진")

    st.image(
        image,
        use_container_width=True
    )


    # ======================================
    # STEP 7. 그림체 선택
    # ======================================

    st.subheader("🎨 애니메이션 그림체 선택")

    style = st.selectbox(
        "원하는 그림체를 선택하세요.",
        [
            "디즈니풍",
            "픽사풍",
            "한국 웹툰풍"
        ],
        key="anime_style"
    )

    st.caption(
        f"선택한 그림체: {style}"
    )


    # ======================================
    # STEP 8. 이미지 변환
    # ======================================

    if st.button(
        "✨ 애니메이션으로 변환하기",
        use_container_width=True
    ):

        with st.spinner(
            "AI가 사진을 변환하고 있습니다. 잠시만 기다려 주세요..."
        ):

            try:

                anime_result = convert_to_anime(
                    image,
                    style
                )

                st.success(
                    "애니메이션 변환이 완료되었습니다!"
                )

                # 원본과 결과 비교
                st.subheader("✨ 변환 결과")

                col1, col2 = st.columns(2)

                with col1:

                    st.image(
                        image,
                        caption="원본 사진",
                        use_container_width=True
                    )

                with col2:

                    st.image(
                        anime_result,
                        caption=style,
                        use_container_width=True
                    )

                # 다운로드
                buffer = io.BytesIO()

                anime_result.save(
                    buffer,
                    format="PNG"
                )

                st.download_button(
                    label="📥 변환된 사진 다운로드",
                    data=buffer.getvalue(),
                    file_name="anime_studio_result.png",
                    mime="image/png",
                    use_container_width=True
                )

            except Exception as e:

                st.error(
                    f"이미지 변환 오류: {e}"
                )

else:

    st.info(
        "사진을 업로드하거나 카메라로 촬영해 주세요."
    )


# ==========================================
# STEP 9. 하단 안내
# ==========================================

st.divider()

st.caption(
    "Anime Studio | Powered by OpenAI Image API."
)
