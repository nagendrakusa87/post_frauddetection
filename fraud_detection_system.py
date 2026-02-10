class FraudDetectionSystem:
    def score_text(self, text):
        # Placeholder scoring logic for text
        return len(text) % 10  # Simple score based on text length

    def score_photo(self, image_url):
        # Placeholder scoring logic for photos
        return 5 if 'fraud' in image_url else 1  # Simple heuristic

    def score_video(self, video_url):
        # Placeholder scoring logic for videos
        return 7 if 'fraud' in video_url else 2  # Simple heuristic

# Example usage
if __name__ == "__main__":
    fds = FraudDetectionSystem()
    print(fds.score_text("This is a sample text post."))
    print(fds.score_photo("http://example.com/fraud_photo.jpg"))
    print(fds.score_video("http://example.com/video.mp4"))
