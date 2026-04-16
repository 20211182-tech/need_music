# 음악이 필요해 🎵

원형 연결 리스트(Circular Linked List)를 이용한 음악 플레이리스트 관리 프로젝트

## 프로젝트 개요

이 프로젝트는 연결 리스트 자료구조를 활용하여 음악 플레이리스트를 구현합니다.
- **노드(Node)**: 음악 정보와 다음 노드의 포인터 저장
- **플레이리스트(Playlist)**: 원형 연결 리스트로 구현된 음악 관리 시스템

## 주요 기능

### 1. 노드 클래스 (Node)
- 음악 데이터 저장
- 다음 노드 포인터 연결

### 2. 플레이리스트 클래스 (Playlist)

#### add_music(music_name)
플레이리스트에 새로운 노래 추가
```python
playlist_obj.add_music("봄날.mp3")
```

#### remove_music(music_name)
플레이리스트에서 특정 노래 삭제
```python
playlist_obj.remove_music("봄날.mp3")
```

#### play_music(play_mode, music_name)
음악 재생 모드
- **normal**: 순차 재생 (모든 노래를 순서대로 재생)
- **repeat**: 반복 재생 (무한 반복)
- **single**: 단일 재생 (특정 노래만 재생)

```python
playlist_obj.play_music("normal")  # 순차 재생
playlist_obj.play_music("single", "봄날.mp3")  # 특정 곡 재생
```

#### display_playlist()
현재 플레이리스트의 모든 노래 표시
```python
playlist_obj.display_playlist()
```

## 사용 예시

```python
# 플레이리스트 생성
playlist_obj = playlist()

# 노래 추가
playlist_obj.add_music("뱅뱅뱅.mp3")
playlist_obj.add_music("봄날.mp3")
playlist_obj.add_music("마음.mp3")

# 플레이리스트 표시
playlist_obj.display_playlist()

# 순차 재생
playlist_obj.play_music("normal")

# 특정 곡만 재생
playlist_obj.play_music("single", "봄날.mp3")

# 노래 삭제
playlist_obj.remove_music("봄날.mp3")
```

## 실행 방법

```bash
python need_music.py
```

## 필요한 라이브러리

- Python 3.6+
- playsound (선택사항, 실제 음악 파일 재생 시)

```bash
pip install playsound
```

## 자료구조: 원형 연결 리스트

```
┌─────┐      ┌─────┐      ┌─────┐
│ 뱅뱅뱅 │ --> │ 봄날  │ --> │ 마음  │
└─────┘      └─────┘      └─────┘
    ↑                          │
    └──────────────────────────┘
```

마지막 노드가 첫 번째 노드를 가리켜 원형을 형성합니다.

## 시간 복잡도

| 작업 | 복잡도 |
|------|--------|
| add_music | O(n) |
| remove_music | O(n) |
| play_music | O(n) |
| display_playlist | O(n) |

## 라이선스

자유롭게 사용 가능합니다.
