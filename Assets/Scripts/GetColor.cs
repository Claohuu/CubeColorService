using UnityEngine;
using UnityEngine.Networking;
using System.Collections;

public class GetColor : MonoBehaviour {

    public float fetchInterval = 1.0f;

    void Start() {
        StartCoroutine(FetchColorLoop());
    }

    IEnumerator FetchColorLoop() {
        while (true) {
            
            UnityWebRequest request = UnityWebRequest.Get("http://localhost:8080/color");

            yield return request.SendWebRequest();

            if (request.result == UnityWebRequest.Result.Success) {
                ColorData data = JsonUtility.FromJson<ColorData>(request.downloadHandler.text);

                Renderer renderer = GetComponent<Renderer>();
                renderer.material.color = new Color(data.r, data.g, data.b);

            } else {
                Debug.LogError("Can't get color: " + request.error);
            }

            yield return new WaitForSeconds(fetchInterval);
        }
    }
}

[System.Serializable]
public class ColorData {
    public float r;
    public float g;
    public float b;
}