# 음악이 필요해 🎵

원형 연결 리스트(Circular Linked List)를 이용한 음악 플레이리스트 관리 프로젝트

## 프로젝트 개요

연결 리스트 자료구조를 활용하여 음악 플레이리스트를 완벽하게 구현한 프로젝트입니다.

### 자료구조: 원형 연결 리스트
```
┌─────┐      ┌─────┐      ┌─────┐
│ 곡1  │ --> │ 곡2  │ --> │ 곡3  │
└─────┘      └─────┘      └─────┘
    ↑                          │
    └──────────────────────────┘
```
마지막 노드가 첫 번째 노드를 가리켜 원형을 형성합니다.

## 주요 기능

### 1. 노드 클래스 (Node)
```python
class Node:
    def __init__(self, data):
        self.data = data  # 음악 정보
        self.next = None  # 다음 노드 포인터
```

### 2. 플레이리스트 클래스 (Playlist)

#### add_music(music_name)
플레이리스트에 새로운 노래 추가
```python
playlist.add_music("봄날.mp3")
# [+] '봄날.mp3' 추가됨
```

#### remove_music(music_name)
플레이리스트에서 특정 노래 삭제
```python
playlist.remove_music("봄날.mp3")
# [-] '봄날.mp3' 삭제됨
```

#### play_music(play_mode, music_name, repeat_count)
음악 재생 모드
- **normal**: 순차 재생 (모든 노래를 순서대로 재생)
- **single**: 단곡 재생 (특정 노래만 재생)
- **repeat**: 반복 재생 (지정한 횟수만큼 반복)

```python
# 순차 재생
playlist.play_music("normal")

# 특정 곡 재생
playlist.play_music("single", "봄날.mp3")

# 2회 반복 재생
playlist.play_music("repeat", repeat_count=2)
```

#### display_playlist()
현재 플레이리스트 표시
```python
playlist.display_playlist()
# ==============================
#      현재 플레이리스트
# ==============================
#  1. 뱅뱅뱅.mp3
#  2. 봄날.mp3
#  3. 마음.mp3
# ==============================
```

#### search_music(music_name)
특정 노래 검색
```python
if playlist.search_music("봄날.mp3"):
    print("찾음")
```

#### get_size()
플레이리스트 곡 개수 조회
```python
count = playlist.get_size()
print(f"총 {count}곡")
```

## 사용 예시

```python
# 플레이리스트 생성
playlist = Playlist()

# 노래 추가
playlist.add_music("뱅뱅뱅.mp3")
playlist.add_music("봄날.mp3")
playlist.add_music("마음.mp3")

# 플레이리스트 표시
playlist.display_playlist()

# 순차 재생
playlist.play_music("normal")

# 특정 곡만 재생
playlist.play_music("single", "봄날.mp3")

# 2회 반복 재생
playlist.play_music("repeat", repeat_count=2)

# 노래 검색
if playlist.search_music("봄날.mp3"):
    print("봄날.mp3 찾음")

# 노래 삭제
playlist.remove_music("봄날.mp3")

# 플레이리스트 크기 확인
print(f"남은 곡: {playlist.get_size()}곡")
```

## 실행 방법

```bash
python need_music.py
```

## 필요한 환경

- Python 3.6+
- 추가 라이브러리 필요 없음

## 시간 복잡도

| 작업 | 복잡도 | 설명 |
|------|--------|------|
| add_music | O(n) | 마지막 노드를 찾아야 함 |
| remove_music | O(n) | 삭제할 노드를 찾아야 함 |
| play_music | O(n) | 모든 노드를 순회 |
| search_music | O(n) | 노래를 찾을 때까지 순회 |
| display_playlist | O(n) | 모든 노드를 순회하며 출력 |

## 공간 복잡도

**O(n)** - n개의 노래를 저장

## 테스트 결과

모든 주요 기능이 정상적으로 작동합니다:
- ✅ 노래 추가
- ✅ 노래 삭제
- ✅ 순차 재생
- ✅ 단곡 재생
- ✅ 반복 재생
- ✅ 노래 검색
- ✅ 플레이리스트 표시

## 라이선스

자유롭게 사용 가능합니다.
