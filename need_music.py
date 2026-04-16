class Node:
    """노드 클래스: 데이터와 다음 노드 포인터를 저장"""
    def __init__(self, data):
        self.data = data
        self.next = None
        
head = None
posHEAD = 0
posTAIL = 1
posNODE = 2


def insert(data, position=posHEAD, node=None):
    """연결 리스트에 새로운 항목 추가"""
    global head
    
    new_node = Node(data)
    
    # 1. 리스트가 비어있는 경우
    if head is None:
        head = new_node
        return
    
    # 2. 헤드에 삽입
    if position == posHEAD:
        new_node.next = head
        head = new_node
        return
    
    # 3. 테일에 삽입
    if position == posTAIL:
        current = head
        while current.next is not None:
            current = current.next
        current.next = new_node
        return
    
    # 4. 특정 노드 뒤에 삽입
    if position == posNODE and node is not None:
        current = head
        while current and current.data != node:
            current = current.next
        
        if current is None:
            print("지정된 노드를 찾을 수 없습니다.")
            return
        
        new_node.next = current.next
        current.next = new_node
        
def delete(position=posHEAD, node=None):
    """연결 리스트에서 항목 삭제"""
    global head
    
    # 1. 리스트가 비어있는 경우
    if head is None:
        print("리스트가 비어 있습니다.")
        return
    
    # 2. 헤드 삭제
    if position == posHEAD:
        head = head.next
        return
    
    # 3. 테일 삭제
    if position == posTAIL:
        current = head
        prev = None
        while current.next is not None:
            prev = current
            current = current.next
        if prev is not None:
            prev.next = None
        return


class playlist:
    """플레이리스트 클래스: 원형 연결 리스트로 구현"""
    def __init__(self):
        self.head = None
    
    def play_music(self, play_mode="normal",music_name=None):
        if self.head is None:
            print("플레이리스트가 비어 있습니다.")
            return
        current = self.head
        
        if play_mode == "repeat":
            while True:
                print(f"현재 노래: {current.data}")
                play(current.data)
                current = current.next if current else self.head
        elif play_mode == "single":
            if music_name is None:
                print("노래 이름을 입력해주세요.")
                return
            while current:
                if current.data == music_name:
                    print(f"현재 노래: {current.data}")
                    play(current.data)
                    return
                current = current.next
            print("노래를 찾을 수 없습니다.")
        else:  # normal mode
            current = self.head
            while current:
                print(f"현재 노래: {current.data}")
                play(current.data)
                current = current.next
    
    def add_music(self, music_name):
        """플레이리스트에 노래 추가"""
        new_node = Node(music_name)
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # 원형 연결 리스트
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
    
    def remove_music(self, music_name):
        """플레이리스트에서 노래 삭제"""
        if self.head is None:
            print("플레이리스트가 비어 있습니다.")
            return
        
        if self.head.data == music_name:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            print(f"'{music_name}' 노래가 삭제되었습니다.")
            return
        
        current = self.head
        while current.next != self.head:
            if current.next.data == music_name:
                current.next = current.next.next
                print(f"'{music_name}' 노래가 삭제되었습니다.")
                return
            current = current.next
        print("노래를 찾을 수 없습니다.")
    
    def display_playlist(self):
        """플레이리스트 전체 표시"""
        if self.head is None:
            print("플레이리스트가 비어 있습니다.")
            return
        
        print("\n=== 플레이리스트 ===")
        current = self.head
        count = 1
        while True:
            print(f"{count}. {current.data}")
            current = current.next
            count += 1
            if current == self.head:
                break
        print()


def play(music_name):
    """음악 재생 함수"""
    print(f"🎵 '{music_name}' 재생 중...")
    # playsound 사용 시 실제 음악 파일 경로 필요
    # from playsound import playsound
    # playsound(music_name)


if __name__ == "__main__":
    # 테스트 코드
    playlist_obj = playlist()
    
    # 플레이리스트에 노래 추가
    playlist_obj.add_music("뱅뱅뱅.mp3")
    playlist_obj.add_music("봄날.mp3")
    playlist_obj.add_music("마음.mp3")
    
    # 플레이리스트 표시
    playlist_obj.display_playlist()
    
    # 일반 재생 (순차 재생)
    print("\n--- 순차 재생 ---")
    playlist_obj.play_music("normal")
    
    # 반복 재생
    print("\n--- 1곡 반복 재생 (3회만) ---")
    # playlist_obj.play_music("repeat")  # 무한 반복이므로 주석 처리
    
    # 단일 재생
    print("\n--- 특정 곡 재생 ---")
    playlist_obj.play_music("single", "봄날.mp3")
    
    # 노래 삭제
    print("\n--- 노래 삭제 ---")
    playlist_obj.remove_music("봄날.mp3")
    
    # 삭제 후 플레이리스트
    print("\n--- 삭제 후 플레이리스트 ---")
    playlist_obj.display_playlist()
