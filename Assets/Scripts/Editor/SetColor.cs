using UnityEngine;
using UnityEditor;
using System.Text;
using System.Net.Http;

[CustomEditor(typeof(GetColor))]
public class SetColor : Editor {
    private Color selectedColor = Color.red;

    public override void OnInspectorGUI() {
        DrawDefaultInspector();

        GUILayout.Space(10);

        selectedColor = EditorGUILayout.ColorField("Color", selectedColor);

        if (GUILayout.Button("Set Color")) {
            SendColor(selectedColor);
        }
    }

    private async void SendColor(Color color) {
        string json = JsonUtility.ToJson(new ColorData {
            r = color.r,
            g = color.g,
            b = color.b
        });

        using (HttpClient client = new HttpClient()) {
            var content = new StringContent(json, Encoding.UTF8, "application/json");
            await client.PostAsync("http://localhost:8080/color", content);
            Debug.Log("Color sent :D");
        }
    }
}