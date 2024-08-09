{{- define "service.listInitPulseEnvVariables" -}}
{{- range $key, $val := .Values.pulse.env.secret }}
- name: {{ $key }}
  valueFrom:
    secretKeyRef:
      name: {{ $.Values.secret.name }}
      key: {{ $key }}
{{- end}}
{{- range $key, $val := .Values.pulse.env.normal }}
- name: {{ $key }}
  value: {{ $val | quote }}
{{- end}}
{{- end }}
