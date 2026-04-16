# -*- coding: utf-8 -*-
"""
음악이 필요해: 원형 연결 리스트 기반 음악 플레이리스트 관리 시스템
"""


class Node:
    """노드 클래스: 데이터와 다음 노드 포인터를 저장"""
    def __init__(self, data):
        self.data = data
        self.next = None


class Playlist:
    """플레이리스트 클래스: 원형 연결 리스트로 구현"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def add_music(self, music_name):
        """플레이리스트에 노래 추가"""
        new_node = Node(music_name)
        
        if self.head is None:
            self.head = new_node
            new_node.next = self.head  # 원형 연결
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
        
        self.size += 1
        print(f"[+] '{music_name}' 추가됨")
    
    def remove_music(self, music_name):
        """플레이리스트에서 노래 삭제"""
        if self.head is None:
            print("[-] 플레이리스트가 비어 있습니다.")
            return
        
        # 헤드 노드 삭제
        if self.head.data == music_name:
            if self.head.next == self.head:
                self.head = None
            else:
                current = self.head
                while current.next != self.head:
                    current = current.next
                current.next = self.head.next
                self.head = self.head.next
            self.size -= 1
            print(f"[-] '{music_name}' 삭제됨")
            return
        
        # 다른 노드 삭제
        current = self.head
        while current.next != self.head:
            if current.next.data == music_name:
                current.next = current.next.next
                self.size -= 1
                print(f"[-] '{music_name}' 삭제됨")
                return
            current = current.next
        
        print(f"[-] '{music_name}'을(를) 찾을 수 없습니다.")
    
    def display_playlist(self):
        """플레이리스트 전체 표시"""
        if self.head is None:
            print("\n[*] 플레이리스트가 비어 있습니다.\n")
            return
        
        print("\n" + "="*30)
        print("     현재 플레이리스트")
        print("="*30)
        current = self.head
        count = 1
        while True:
            print(f"{count:2d}. {current.data}")
            current = current.next
            count += 1
            if current == self.head:
                break
        print("="*30 + "\n")
    
    def play_music(self, play_mode="normal", music_name=None, repeat_count=1):
        """
        음악 재생
        - play_mode: 'normal'(순차), 'single'(단곡), 'repeat'(반복)
        - music_name: single 모드일 때 재생할 곡명
        - repeat_count: 반복 횟수
        """
        if self.head is None:
            print("[-] 플레이리스트가 비어 있습니다.")
            return
        
        if play_mode == "normal":
            self._play_normal()
        elif play_mode == "single":
            self._play_single(music_name)
        elif play_mode == "repeat":
            self._play_repeat(repeat_count)
        else:
            print("[-] 잘못된 재생 모드입니다.")
    
    def _play_normal(self):
        """순차 재생"""
        print("\n[PLAY] 순차 재생 시작")
        print("-" * 30)
        current = self.head
        count = 0
        while count < self.size:
            print(f">>> {current.data} 재생 중...")
            current = current.next
            count += 1
        print("-" * 30)
        print("[PLAY] 재생 완료\n")
    
    def _play_single(self, music_name):
        """단곡 재생"""
        if music_name is None:
            print("[-] 재생할 곡명을 입력해주세요.")
            return
        
        current = self.head
        count = 0
        while count < self.size:
            if current.data == music_name:
                print(f"\n[PLAY] 단곡 재생: {music_name}")
                print("-" * 30)
                print(f">>> {current.data} 재생 중...")
                print("-" * 30 + "\n")
                return
            current = current.next
            count += 1
        
        print(f"[-] '{music_name}'을(를) 찾을 수 없습니다.")
    
    def _play_repeat(self, repeat_count):
        """반복 재생"""
        if repeat_count <= 0:
            repeat_count = 1
        
        print(f"\n[PLAY] {repeat_count}회 반복 재생 시작")
        print("-" * 30)
        for i in range(repeat_count):
            current = self.head
            count = 0
            while count < self.size:
                print(f">>> [{i+1}/{repeat_count}] {current.data} 재생 중...")
                current = current.next
                count += 1
        print("-" * 30)
        print("[PLAY] 재생 완료\n")
    
    def get_size(self):
        """플레이리스트 크기 반환"""
        return self.size
    
    def search_music(self, music_name):
        """노래 검색"""
        if self.head is None:
            return False
        
        current = self.head
        count = 0
        while count < self.size:
            if current.data == music_name:
                return True
            current = current.next
            count += 1
        return False


def main():
    """메인 함수"""
    print("\n" + "="*40)
    print("음악이 필요해 - 플레이리스트 관리 프로그램")
    print("="*40 + "\n")
    
    playlist = Playlist()
    
    # 테스트: 노래 추가
    print("[테스트 1] 노래 추가")
    print("-" * 40)
    playlist.add_music("뱅뱅뱅.mp3")
    playlist.add_music("봄날.mp3")
    playlist.add_music("마음.mp3")
    playlist.add_music("Dynamite.mp3")
    print()
    
    # 테스트: 플레이리스트 표시
    print("[테스트 2] 플레이리스트 표시")
    playlist.display_playlist()
    
    # 테스트: 순차 재생
    print("[테스트 3] 순차 재생")
    playlist.play_music("normal")
    
    # 테스트: 단곡 재생
    print("[테스트 4] 단곡 재생")
    playlist.play_music("single", "봄날.mp3")
    
    # 테스트: 반복 재생
    print("[테스트 5] 2회 반복 재생")
    playlist.play_music("repeat", repeat_count=2)
    
    # 테스트: 노래 검색
    print("[테스트 6] 노래 검색")
    print("-" * 40)
    result = playlist.search_music("봄날.mp3")
    print(f"'봄날.mp3' 검색: {'찾음' if result else '못 찾음'}")
    result = playlist.search_music("존재하지않는곡.mp3")
    print(f"'존재하지않는곡.mp3' 검색: {'찾음' if result else '못 찾음'}")
    print()
    
    # 테스트: 노래 삭제
    print("[테스트 7] 노래 삭제")
    print("-" * 40)
    playlist.remove_music("봄날.mp3")
    print()
    
    # 테스트: 삭제 후 플레이리스트
    print("[테스트 8] 삭제 후 플레이리스트")
    playlist.display_playlist()
    
    # 테스트: 플레이리스트 크기
    print("[테스트 9] 플레이리스트 정보")
    print("-" * 40)
    print(f"현재 곡 개수: {playlist.get_size()}곡\n")


if __name__ == "__main__":
    main()
